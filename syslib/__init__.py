from importer import importer
importer("../../pyltr/pyltr", __file__)

from pyltr import parse_flat
from pathlib import Path
def add_sysdep(gid):
	if isinstance(gid, tuple):
		gid = list(gid)
	assert isinstance(gid, list)
	assert gid[:3] == ["com", "6e5d", "syslib"]
	filename  = "_".join(gid[3:]) + ".ltr"
	path = Path(__file__).parent.parent / "data" / filename
	s = open(path).read()
	ltr = parse_flat(s)
	d = dict()
	for line in ltr:
		d[line[0]] = line[1:]
	return d

def symtable(gids):
	lookup = dict()
	gids += [
		["com", "6e5d", "syslib", "std", "stdlib"],
		["com", "6e5d", "syslib", "std", "string"],
		["com", "6e5d", "syslib", "std", "stdio"],
		["com", "6e5d", "syslib", "std", "assert"],
		["com", "6e5d", "syslib", "std", "time"],
		["com", "6e5d", "syslib", "std", "math"],
		["com", "6e5d", "syslib", "posix", "fcntl"],
		["com", "6e5d", "syslib", "posix", "unistd"],
		["com", "6e5d", "syslib", "posix", "sys", "stat"],
		["com", "6e5d", "syslib", "posix", "sys", "types"],
	]
	for gid in gids:
		d = add_sysdep(gid)
		for symbol in d["symbols"]:
			if symbol in lookup:
				raise Exception("collision")
			lookup[symbol] = gid
	return lookup
