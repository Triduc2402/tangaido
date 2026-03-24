import tkinter as tk

def create_heart():
    root = tk.Tk()
    root.title("Gửi tặng bạn ❤️")
    root.geometry("500x500")
    root.configure(bg='black')

    heart_txt = (
        "      .........           .........      \n"
        "   ...............     ...............   \n"
        " ................... ................... \n"
        ".........................................\n"
        ".........................................\n"
        " ....................................... \n"
        "  .....................................  \n"
        "    .................................    \n"
        "      .............................      \n"
        "        .........................        \n"
        "          .....................          \n"
        "            .................            \n"
        "              .............              \n"
        "                .........                \n"
        "                  .....                  \n"
        "                    .                    "
    )
    label = tk.Label(
        root, 
        text=heart_txt, 
        fg='#FF3030', # Màu đỏ rực
        bg='black', 
        font=('Courier New', 12, 'bold'),
        justify='center'
    )
    label.pack(expand=True)

    footer = tk.Label(root, text="Love you!", fg='white', bg='black', font=('Arial', 10, 'italic'))
    footer.pack(side='bottom', pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_heart()