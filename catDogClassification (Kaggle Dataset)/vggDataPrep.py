def dataSeparator(datasetPath, limit):
    import os
    import shutil

    # Path Creation
    dataFolder = "/data"
    customDatasetPath = "data/dataset"+str(limit)
    cat = ("data/dataset"+str(limit)+ "/cat")
    dog = ("data/dataset"+str(limit)+ "/dog")

    # Creating if the Directory Exist:
    if not os.path.exists(dataFolder):
        os.mkdir(dataFolder)
    if not os.path.exists(customDatasetPath):
        os.mkdir(customDatasetPath)
    if not os.path.exists(cat):
        os.mkdir(cat)
    if not os.path.exists(dog):
        os.mkdir(dog)

    if os.path.exists(cat):
        iptUsr = input("! FolderExist: Do you want to replace the content of the Folders? (y/n) ")
        if iptUsr == "y":
            shutil.rmtree(cat)
            shutil.rmtree(dog)
            os.mkdir(cat)
            os.mkdir(dog)
        print("--> Appending to the Current Directory Content")


    # Loading the Dataset File
    files = os.listdir(datasetPath)
    count = 0
    print("\nSize of Dataset: ", len(files))

    # We need this limit to Ensure that Cat & Dog
    # Example are balance:
    catLimit = 0
    dogLimit = 0
    balanceLimit = limit / 2

    for file in files:

        if catLimit == dogLimit == balanceLimit:
            break

        src_path = os.path.join(datasetPath, file)

        if len(file.split(".")) > 1:

            if file.split(".")[0] == 'cat' and catLimit != balanceLimit:
                dst_path = os.path.join(cat, file)
                # print(src_path, dst_path)
                os.rename(src_path, dst_path)
                catLimit += 1


            elif file.split(".")[0] == 'dog' and dogLimit != balanceLimit:
                dst_path = os.path.join(dog, file)
                os.rename(src_path, dst_path)
                dogLimit += 1

        # print(catLimit, " | ", dogLimit)
    print("\n====== Custom Dataset Successfully Created! ======  \n")
    return (customDatasetPath, cat, dog)

def splitCustomDataset(customDatasetPath, cat, dog,
                        train:float, test:float):
    import os
    import shutil

    # cat = "/mnt/e/wk/pyTorch/help/prac/data/catDogDataset/cat/"
    # dog = "/mnt/e/wk/pyTorch/help/prac/data/catDogDataset/dog/"

    trainPath = customDatasetPath + "/train"
    testPath = customDatasetPath + "/test"

    # Creating if the Directory Exist:
    if not os.path.exists(trainPath):
        os.mkdir(trainPath)
        os.mkdir(trainPath + "/cat")
        os.mkdir(trainPath + "/dog")
    if not os.path.exists(testPath):
        os.mkdir(testPath)
        os.mkdir(testPath + "/cat")
        os.mkdir(testPath + "/dog")

    # Checking if the Folder Exist & What to do with It:
    if os.path.exists(trainPath):
        iptUsr = input("! FolderExist: Do you want to replace the content of the Folders? (y/n) ")
        if iptUsr == "y":
            shutil.rmtree(trainPath)
            shutil.rmtree(testPath)

            os.mkdir(trainPath)
            os.mkdir(trainPath + "/cat")
            os.mkdir(trainPath + "/dog")

            os.mkdir(testPath)
            os.mkdir(testPath + "/cat")
            os.mkdir(testPath + "/dog")
        print("--> Appending to the Current Directory Content")

    count = 0
    catFiles = os.listdir(cat)
    dogFiles = os.listdir(dog)

    balanceLimit = len(catFiles)
    trainLength = balanceLimit * train
    testLength = balanceLimit * test

    # print(catFiles)
    print(balanceLimit, " | ", trainLength, " | ", testLength)

    flag = 0

    for catFile in catFiles:

        src_path = os.path.join(cat, catFile)

        if count == trainLength:
            count = 0
            flag = 1

        # print(count)
        if count != trainLength and flag == 0:
            dst_path = os.path.join(trainPath + "/cat", catFile)
            shutil.copy(src_path, dst_path)
            count += 1
            continue

        if count != testLength and flag == 1:
            dst_path = os.path.join(testPath + "/cat", catFile)
            shutil.copy(src_path, dst_path)
            count += 1
            continue

    flag = 0
    count = 0

    for dogFile in dogFiles:

        src_path = os.path.join(dog, dogFile)

        if count == trainLength:
            count = 0
            flag = 1

        # print(count)
        if count != trainLength and flag == 0:
            dst_path = os.path.join(trainPath + "/dog", dogFile)
            shutil.copy(src_path, dst_path)
            count += 1
            continue

        if count != testLength and flag == 1:
            dst_path = os.path.join(testPath + "/dog", dogFile)
            shutil.copy(src_path, dst_path)
            count += 1
            continue

    print("\n====== Train / Test Split Successfully Executed! ======  \n")

# customDatasetPath, catPath, dogPath = dataSeparator("data/CAT_DOG", 500)
# splitCustomDataset(customDatasetPath, catPath, dogPath, 0.8, 0.2)
