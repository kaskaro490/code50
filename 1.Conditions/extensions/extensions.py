filename = input("File name: ").lower()

if filename.endswith(.gif):
    print("image/gif")
elif filename.endswith(.jpg):
    print("image/jpg")
elif filename.endswith(.jpeg):
    print("image/jpg")
elif filename.endswith(.png):
    print("image/png")
elif filename.endswith(.pdf):
    print("application/pdf")
elif filename.endswith(.zip):
    print("application/zip")
elif filename.endswith(.txt):
    print("text/plain")

else:
    print("application/octet-stream")








