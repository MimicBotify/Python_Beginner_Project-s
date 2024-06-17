# TAKE PHOTO IF PASSWORD IS INCORRECT
import cv2

secret_password = "mothertrucker"


def take_photo():
    cap = cv2.VideoCapture(0)
    path = 'C:\\Users\\DELL\\OneDrive\\Desktop\\Python Beginner Practice\\Photo\\Captured Photo.jpg'
    if not cap:
        print("Having Error opening the camera.")
        exit()
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(path, frame)
        print("Captured photo")
    cap.release()
    cv2.destroyAllWindows()


def main():
    password = ""
    tries = 0
    spy = True
    while password != secret_password and spy:
        password = input("Enter the password: ")
        tries += 1
        if password == secret_password:
            print("Correct password")
            spy = False
        elif tries == 3:
            take_photo()
            print('Captured Photo')
            break
        else:
            print("Try again!")


if __name__ == '__main__':
    main()
