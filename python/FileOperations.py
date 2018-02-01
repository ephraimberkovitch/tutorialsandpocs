from datetime import datetime

fo = open("c:\\temp\\jenkins_test.txt", "a")
fo.write(str(datetime.now()))
fo.write("\n")
fo.close()