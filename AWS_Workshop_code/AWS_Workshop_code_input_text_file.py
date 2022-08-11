def open_input(file):
    with open(file, 'r') as f:
        text = f.read()
        print(text)
        

def main():
    open_input("text.txt")
    
if __name__=="__main__":
    main()