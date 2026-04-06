layout = '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/bg_main_gradient"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="28dp">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="SELECT CATEGORY"
        android:textColor="@color/gold"
        android:textSize="28sp"
        android:textStyle="bold"
        android:letterSpacing="0.12"
        android:gravity="center"
        android:layout_marginBottom="36dp"/>

    <Button
        android:id="@+id/btnCaribbeanHistory"
        android:layout_width="match_parent"
        android:layout_height="68dp"
        android:layout_marginBottom="14dp"
        android:background="@drawable/bg_button_accent"
        android:backgroundTint="@null"
        android:stateListAnimator="@null"
        android:text="&#127758;  CARIBBEAN HISTORY"
        android:textColor="@color/gold"
        android:textSize="15sp"
        android:textStyle="bold"
        android:letterSpacing="0.08"/>

    <Button
        android:id="@+id/btnScienceTech"
        android:layout_width="match_parent"
        android:layout_height="68dp"
        android:layout_marginBottom="14dp"
        android:background="@drawable/bg_button_accent"
        android:backgroundTint="@null"
        android:stateListAnimator="@null"
        android:text="&#128300;  SCIENCE &amp; TECH"
        android:textColor="@color/gold"
        android:textSize="15sp"
        android:textStyle="bold"
        android:letterSpacing="0.08"/>

    <Button
        android:id="@+id/btnSports"
        android:layout_width="match_parent"
        android:layout_height="68dp"
        android:layout_marginBottom="14dp"
        android:background="@drawable/bg_button_accent"
        android:backgroundTint="@null"
        android:stateListAnimator="@null"
        android:text="&#9917;  SPORTS"
        android:textColor="@color/gold"
        android:textSize="15sp"
        android:textStyle="bold"
        android:letterSpacing="0.08"/>

    <Button
        android:id="@+id/btnWorldGeography"
        android:layout_width="match_parent"
        android:layout_height="68dp"
        android:layout_marginBottom="14dp"
        android:background="@drawable/bg_button_accent"
        android:backgroundTint="@null"
        android:stateListAnimator="@null"
        android:text="&#128506;  WORLD GEOGRAPHY"
        android:textColor="@color/gold"
        android:textSize="15sp"
        android:textStyle="bold"
        android:letterSpacing="0.08"/>

    <Button
        android:id="@+id/btnArtsAndCulture"
        android:layout_width="match_parent"
        android:layout_height="68dp"
        android:layout_marginBottom="14dp"
        android:background="@drawable/bg_button_accent"
        android:backgroundTint="@null"
        android:stateListAnimator="@null"
        android:text="&#127912;  ARTS &amp; CULTURE"
        android:textColor="@color/gold"
        android:textSize="15sp"
        android:textStyle="bold"
        android:letterSpacing="0.08"/>

    <Button
        android:id="@+id/btnSvgVincyLife"
        android:layout_width="match_parent"
        android:layout_height="68dp"
        android:background="@drawable/bg_button_accent"
        android:backgroundTint="@null"
        android:stateListAnimator="@null"
        android:text="&#127988;  SVG &amp; VINCY LIFE"
        android:textColor="@color/gold"
        android:textSize="15sp"
        android:textStyle="bold"
        android:letterSpacing="0.08"/>

</LinearLayout>'''

with open("./app/src/main/res/layout/activity_category.xml", "w") as f:
    f.write(layout)
print("Done")
