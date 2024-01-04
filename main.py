import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk
from rembg import remove


class BackgroundRemovalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.image_frame = tk.Frame(self.root, bg="white")
        self.image_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.image_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        bg_image = Image.open("background_image.jpg")
        bg_image = ImageTk.PhotoImage(bg_image)
        self.background_label = tk.Label(self.canvas, image=bg_image)
        self.background_label.image = bg_image
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_label = tk.Label(self.background_label, text="Background Remover", font=("Helvetica", 24), bg="white")
        title_label.pack(pady=20)

        self.browse_button = tk.Button(self.background_label, text="Browse and Remove Background",
                                       command=self.remove_background,
                                       font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=20, pady=10)
        self.browse_button.pack(pady=20)

    def remove_background(self):
        input_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.ppm *.pgm")])

        if not input_path:
            return

        try:
            output_path = 'output.png'
            input_image = Image.open(input_path)
            output_image = remove(input_image)
            output_image.save(output_path)

            self.show_result(output_path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def show_result(self, image_path):
        result_window = tk.Toplevel(self.root)
        result_window.title("Background Removed")

        result_image = Image.open(image_path)
        photo = ImageTk.PhotoImage(result_image)

        label = tk.Label(result_window, image=photo)
        label.image = photo
        label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemovalApp(root)
    root.mainloop()
