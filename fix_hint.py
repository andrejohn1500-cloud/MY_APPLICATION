path = "./app/src/main/res/layout/activity_result.xml"
content = open(path).read()
content = content.replace('android:hintTextColor="#9099B7"', 'android:textColorHint="#9099B7"')
open(path, "w").write(content)
print("Done")
