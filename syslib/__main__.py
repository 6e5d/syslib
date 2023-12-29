from . import add_sysdep
import sys

result = []
for arg in sys.argv[1:]:
	gid = ["com", "6e5d", "syslib", arg]
	d = add_sysdep(gid)
	result += d["apt"]
print(" ".join(result))
