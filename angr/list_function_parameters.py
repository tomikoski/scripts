import angr
import sys

PROCNAME = "list_function_parameters"

if len(sys.argv) < 3:
   print(f"usage: python3 {PROCNAME} crackme main")
   sys.exit(0)

proj = angr.Project(sys.argv[1], auto_load_libs=False)
#cfg = proj.analyses.CFG(normalize=True)
cfg = proj.analyses.CFG(cross_references=True)
#f = cfg.kb.functions[sys.argv[2]]

f = proj.kb.functions[sys.argv[2]]
print(hex(f.addr))
#proj.analyses.VariableRecoveryFast(f=func)
#cc = p.analyses.CallingConvention(

#print(list(cc.prototype.args))
