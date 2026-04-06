import os

main_xml = open("./app/src/main/res/layout/activity_main.xml").read()

# Fix PLAY button
main_xml = main_xml.replace(
    'android:id="@+id/btnStart"',
    'android:id="@+id/btnStart"\n        android:backgroundTint="@null"\n        android:stateListAnimator="@null"'
)

# Fix other buttons
for btn in ['btnLeaderboard', 'btnDonate', 'btnMyStory']:
    main_xml = main_xml.replace(
        f'android:id="@+id/{btn}"',
        f'android:id="@+id/{btn}"\n        android:backgroundTint="@null"\n        android:stateListAnimator="@null"'
    )

with open("./app/src/main/res/layout/activity_main.xml", "w") as f:
    f.write(main_xml)

print("Fixed")
