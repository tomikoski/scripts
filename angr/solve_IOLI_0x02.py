import angr

proj = angr.Project("IOLI/bin-linux/crackme0x01", auto_load_libs=False)
cfg = proj.analyses.CFG()

FIND = 0x08048449
AVOID = 0x0804843b

sm = proj.factory.simulation_manager()
sm.explore(avoid=AVOID, find=FIND)

print(sm.found[0].posix.dumps(0).split(b'\0')[0])
