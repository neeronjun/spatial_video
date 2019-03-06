from rtree import index
idx = index.Index()
left, bottom, right, top = (0.0, 0.0, 1.0, 1.0)
idx.insert(0,(left,bottom,right,top))