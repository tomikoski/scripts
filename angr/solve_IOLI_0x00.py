import angr

def getFuncAddress( funcName, plt=None ):
    found = [
        addr for addr,func in cfg.kb.functions.items()
        if funcName == func.name and (plt is None or func.is_plt == plt)
        ]
    if len( found ) > 0:
        print("Found "+funcName+"'s address at "+hex(found[0])+"!")
        return found[0]
    else:
        raise Exception("No address found for function : "+funcName)

proj = angr.Project("IOLI/bin-linux/crackme0x00", auto_load_libs=False)
cfg = proj.analyses.CFG()
addr = getFuncAddress("main")

print(f"Main: {hex(addr)}")

FIND = 0x08048480
AVOID = 0x08048472

sm = proj.factory.simulation_manager()
sm.explore(avoid=AVOID, find=FIND)

print(sm.found[0].posix.dumps(0).split(b'\0')[0])
