import os
from PIL import Image

max_mtime = 0
for dirname,subdirs,files in os.walk("."):
	for fname in files:
		if fname.endswith('.tif'):
			full_path = os.path.join(dirname, fname)
			mtime = os.stat(full_path).st_mtime
			if mtime > max_mtime:
				max_mtime = mtime
				max_dir = dirname
				max_file = fname

tif_path = os.path.join(max_dir, max_file)
print (tif_path)		
try:
	Image.open(tif_path).convert("L").save(tif_path)
except Exception as e:
	print (e)