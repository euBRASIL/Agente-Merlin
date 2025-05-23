import tkinter as tk
from PIL import Image, ImageTk, Image as PILImage
import threading
import pystray
import sys

class FloatingMerlin(tk.Tk):
    def __init__(self, image_path, frame_width, frame_height):
        super().__init__()

        # Janela sem borda e transparente
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.attributes("-transparentcolor", "black")

        # Sprite sheet
        self.sprite_sheet = PILImage.open(image_path)
        self.frame_width = frame_width
        self.frame_height = frame_height

        self.sheet_width, self.sheet_height = self.sprite_sheet.size
        self.cols = self.sheet_width // self.frame_width
        self.rows = self.sheet_height // self.frame_height
        self.total_frames = self.cols * self.rows

        self.label = tk.Label(self, bg="black")
        self.label.pack()

        # Posição na tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"+{screen_width - 150}+{screen_height - 135}")

        # Controle de animação
        self.animation_frames = []
        self.current_index = 0
        self.running = False

    def play_animation(self, start_frame, num_frames):
        self.animation_frames = []

        for i in range(num_frames):
            index = (start_frame + i) % self.total_frames
            row = index // self.cols
            col = index % self.cols

            x1 = col * self.frame_width
            y1 = row * self.frame_height
            x2 = x1 + self.frame_width
            y2 = y1 + self.frame_height

            self.animation_frames.append((x1, y1, x2, y2))

        self.current_index = 0
        self.running = True
        self.animate()

    def animate(self):
        if not self.running or not self.animation_frames:
            return

        x1, y1, x2, y2 = self.animation_frames[self.current_index]
        frame = self.sprite_sheet.crop((x1, y1, x2, y2))
        frame_image = ImageTk.PhotoImage(frame)

        self.label.config(image=frame_image)
        self.label.image = frame_image

        self.current_index += 1
        if self.current_index >= len(self.animation_frames):
            self.running = False
        else:
            self.after(100, self.animate)


def setup_tray(app):
    def exit_app(icon, item):
        app.after(0, lambda: app.play_animation(639, 40))
        icon.stop()
        app.destroy()
        sys.exit()

    def deitar(icon, item):	app.after(0, lambda: app.play_animation(0, 29))
    def amor(icon, item):	app.after(0, lambda: app.play_animation(30, 17))
    def nota(icon, item):	app.after(0, lambda: app.play_animation(47, 54))
    def email(icon, item):	app.after(0, lambda: app.play_animation(101, 38))
    def ouvir(icon, item):	app.after(0, lambda: app.play_animation(140, 38))
    def tela(icon, item):	app.after(0, lambda: app.play_animation(179, 57))
    def impressao(icon, item):	app.after(0, lambda: app.play_animation(237, 75))
    def gracinha(icon, item):	app.after(0, lambda: app.play_animation(313, 77))
    def sono(icon, item):	app.after(0, lambda: app.play_animation(390, 33))
    def salvar(icon, item):	app.after(0, lambda: app.play_animation(434, 30))
    def assobiar(icon, item):	app.after(0, lambda: app.play_animation(465, 80))
    def pensar(icon, item):	app.after(0, lambda: app.play_animation(547, 8))
    def esquerda(icon, item):	app.after(0, lambda: app.play_animation(557,  5))
    def olhar2x(icon, item):	app.after(0, lambda: app.play_animation(565, 10))
    def direita(icon, item):	app.after(0, lambda: app.play_animation(574, 4))
    def livro(icon, item):	app.after(0, lambda: app.play_animation(581, 32))
    def alongar(icon, item):	app.after(0, lambda: app.play_animation(614, 24))
    def sair(icon, item):	app.after(0, lambda: app.play_animation(639, 40))
    def escrever(icon, item):	app.after(0, lambda: app.play_animation(680, 50))
    def arte(icon, item):	app.after(0, lambda: app.play_animation(725, 25))
    def anima_F(icon, item):	app.after(0, lambda: app.play_animation(750, 50))
    def mascara(icon, item):	app.after(0, lambda: app.play_animation(800, 20))
    def entrar(icon, item):	app.after(0, lambda: app.play_animation(820, 29))
    def cortar(icon, item):	app.after(0, lambda: app.play_animation(894, 20))
    def apontar(icon, item):	app.after(0, lambda: app.play_animation(915, 19))
    def olfato(icon, item):	app.after(0, lambda: app.play_animation(935, 49)) # Animação 985 "some" pois não existe

    def macarico(icon, item):
        tempo_frame = 40 * 100  # 40 quadros x 100ms
        app.play_animation(850, 40) # 1a. animação
        app.after(tempo_frame, lambda: app.play_animation(800, 20)) # 2a. animação





    image = PILImage.new('RGB', (64, 64), color='black')
    icon = pystray.Icon("Merlin", image, menu=pystray.Menu(
        pystray.MenuItem("Deitar e Sentar", deitar),
        pystray.MenuItem("Amor", amor),
        pystray.MenuItem("Nota 10/11", nota),
        pystray.MenuItem("E-mail", email),
        pystray.MenuItem("Audição", ouvir),
        pystray.MenuItem("Fundo da Tela", tela),
        pystray.MenuItem("Impressão", impressao),
        pystray.MenuItem("Gracinha", gracinha),
        pystray.MenuItem("Sono", sono),
        pystray.MenuItem("Salvar", salvar),
        pystray.MenuItem("Assobiar", assobiar),
        pystray.MenuItem("Esquerda", esquerda),
        pystray.MenuItem("Pensar", pensar),
        pystray.MenuItem("Olhar 2x", olhar2x),
        pystray.MenuItem("Direita", direita),
        pystray.MenuItem("Ler Livro", livro),
        pystray.MenuItem("Alongar", alongar),
        pystray.MenuItem("Saída", sair),
        pystray.MenuItem("Escritório", escrever),
        pystray.MenuItem("Nota Arte", arte),
        pystray.MenuItem("Animação F", anima_F),
        pystray.MenuItem("Mascara", mascara),
        pystray.MenuItem("Entrar", entrar),
        pystray.MenuItem("Maçarico", macarico),
        pystray.MenuItem("Cortar", cortar),
        pystray.MenuItem("Apontar", apontar),
        pystray.MenuItem("Olfato", olfato),
        pystray.MenuItem("Sair", exit_app)
    ))
    icon.run()

# Instanciar o app e rodar ícone tray em paralelo
app = FloatingMerlin("map.png", 124, 93)
threading.Thread(target=setup_tray, args=(app,), daemon=True).start()

app.mainloop()
