def show_status(distance):
    if distance < 20:
        print("⚠️ DANGER! Obstacle very close:", distance, "cm")
    elif distance < 50:
        print("⚠️ WARNING! Obstacle ahead:", distance, "cm")
    else:
        print("✅ Area clear:", distance, "cm")
