#Open the door only if the fingerprint matches the stored fingerprint.

finger_print=input("enter your finger print:")
stored_fingerprint="ep908"
if finger_print==stored_fingerprint:
    print("door opens")
else:
    print("not matches")
