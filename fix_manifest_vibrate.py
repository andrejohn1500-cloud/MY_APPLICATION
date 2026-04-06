content = open("./app/src/main/AndroidManifest.xml").read()
if 'VIBRATE' not in content:
    content = content.replace(
        '<manifest ',
        '<manifest\n    xmlns:tools="http://schemas.android.com/tools"\n    '
    ).replace(
        '<application',
        '<uses-permission android:name="android.permission.VIBRATE"/>\n\n    <application'
    )
    open("./app/src/main/AndroidManifest.xml", "w").write(content)
    print("Vibrate permission added")
else:
    print("Already present")
