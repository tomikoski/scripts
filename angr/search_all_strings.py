import angr
import sys

if len(sys.argv) < 3:
   print("usage: python3 search_all_strings.py crackme 5")
   sys.exit(0)

proj = angr.Project(sys.argv[1], auto_load_libs=False)
cfg = proj.analyses.CFG(cross_references=True)
strs: list[str] = []

for md_addr, md in cfg.model.memory_data.items():
    if md.sort == 'string':
       refs = proj.kb.xrefs.get_xrefs_by_dst(md_addr)
       if refs and len(md.content) > int(sys.argv[2]):
          strs.append(md.content.decode('utf-8'))

print(strs)
