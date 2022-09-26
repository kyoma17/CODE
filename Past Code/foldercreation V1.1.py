def make_folders(folder_gen, folder_start, folder_end):
	newpath = "C:\\Users\\MaK23074\\Desktop\\test\\"
	slash = r"\""
	while (folder_gen > 0):
		filename = "B000" + str(folder_start) + " - B000" + str(folder_end)

		createpath = newpath + filename

		os.makedirs(createpath)


		folder_start += 100
		folder_end += 100
		folder_gen -= 1 
