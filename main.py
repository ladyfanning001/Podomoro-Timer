# Import library pygame dan sys
import pygame
import sys
from button import Button  # Import class Button dari file button.py (digunakan untuk membuat tombol interaktif)

# Inisialisasi semua modul pygame
pygame.init()

# Ukuran window aplikasi
WIDTH, HEIGHT = 810, 810
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Membuat jendela utama
pygame.display.set_caption("Pomodoro Timer by Ladya")  # Judul jendela

# Objek clock untuk mengatur frame rate
CLOCK = pygame.time.Clock()

# Load gambar background dan gambar tombol
BACKDROP = pygame.image.load("assets/backdrop.jpg")
WHITE_BUTTON = pygame.image.load("assets/button.png")

# Load font untuk tampilan timer dan statistik
FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 120)
STAT_FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 24)

# Render awal timer (25:00)
timer_text = FONT.render("25:00", True, "#d48589")
timer_text_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2-25))

# Membuat tombol START/STOP, Pomodoro, Short Break, dan Long Break
START_STOP_BUTTON = Button(
    WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#c97676", "#9ab034"
)

POMODORO_BUTTON = Button(
    None, (WIDTH/2-150, HEIGHT/2-140), 120, 30, "Pomodoro", 
    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#f2c2bf", "#9ab034"
)

SHORT_BREAK_BUTTON = Button(
    None, (WIDTH/2, HEIGHT/2-140), 120, 30, "Short Break", 
    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#f2c2bf", "#9ab034"
)

LONG_BREAK_BUTTON = Button(
    None, (WIDTH/2+150, HEIGHT/2-140), 120, 30, "Long Break", 
    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#f2c2bf", "#9ab034"
)

# Durasi dalam detik (untuk penggunaan sebenarnya)
POMODORO_LENGTH = 1500    # 25 menit (1500 detik)
SHORT_BREAK_LENGTH = 300  # 5 menit (300 detik)
LONG_BREAK_LENGTH = 600    # 10 menit (600 detik)

# Durasi pendek untuk testing (uncomment jika ingin testing)
# POMODORO_LENGTH = 10      # 10 detik untuk testing
# SHORT_BREAK_LENGTH = 5    # 5 detik untuk testing
# LONG_BREAK_LENGTH = 8     # 8 detik untuk testing

# Mode timer saat ini
POMODORO_MODE = "pomodoro"
SHORT_BREAK_MODE = "short_break"
LONG_BREAK_MODE = "long_break"
current_mode = POMODORO_MODE

# Waktu yang sedang berjalan, default: Pomodoro
current_seconds = POMODORO_LENGTH

# Statistik penggunaan
completed_pomodoros = 0    # Menghitung jumlah pomodoro yang selesai
total_seconds_focused = 0  # Total waktu fokus dalam detik
pomodoro_streak = 0        # Menghitung berapa pomodoro berturut-turut sebelum long break

# Perlu long break setelah 4 pomodoro
POMODOROS_BEFORE_LONG_BREAK = 4

# Load suara notifikasi
try:
    notification_sound = pygame.mixer.Sound("assets/notification.wav")
except:
    print("Peringatan: File suara notifikasi tidak ditemukan. Timer akan bekerja tanpa suara.")
    notification_sound = None

# Set timer pygame untuk mengirim event setiap 1000ms (1 detik)
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Status apakah timer sedang berjalan atau tidak
started = False
timer_completed = False  # Flag untuk menandakan apakah timer baru saja selesai

# Fungsi untuk mengubah mode timer
def change_mode(mode):
    global current_mode, current_seconds, timer_completed
    
    current_mode = mode
    timer_completed = False
    
    if mode == POMODORO_MODE:
        current_seconds = POMODORO_LENGTH
    elif mode == SHORT_BREAK_MODE:
        current_seconds = SHORT_BREAK_LENGTH
    elif mode == LONG_BREAK_MODE:
        current_seconds = LONG_BREAK_LENGTH

# Fungsi untuk memutar suara notifikasi
def play_notification():
    if notification_sound:
        notification_sound.play()

# Game loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Kalau user klik tombol close window
            pygame.quit()
            sys.exit()

        # Kalau user klik mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Cek apakah tombol START/STOP ditekan
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                started = not started  # Toggle antara mulai/pause timer
                
                # Reset timer_completed saat user memulai timer lagi
                if started:
                    timer_completed = False

            # Kalau tombol Pomodoro ditekan
            if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                change_mode(POMODORO_MODE)
                started = False  # Timer berhenti dulu

            # Kalau tombol Short Break ditekan
            if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                change_mode(SHORT_BREAK_MODE)
                started = False

            # Kalau tombol Long Break ditekan
            if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                change_mode(LONG_BREAK_MODE)
                started = False

            # Ganti teks tombol START/STOP sesuai status started
            if started:
                START_STOP_BUTTON.text_input = "STOP"
            else:
                START_STOP_BUTTON.text_input = "START"
                
            START_STOP_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
            
        # Event timer pygame tiap detik
        if event.type == pygame.USEREVENT and started:
            current_seconds -= 1  # Kurangi 1 detik dari timer
            
            # Cek apakah timer sudah habis
            if current_seconds <= 0:
                # Berhenti dan putar suara notifikasi
                started = False
                play_notification()
                timer_completed = True
                
                # Proses berdasarkan mode yang baru saja selesai
                if current_mode == POMODORO_MODE:
                    # Tambah statistik fokus
                    completed_pomodoros += 1
                    total_seconds_focused += POMODORO_LENGTH
                    pomodoro_streak += 1
                    
                    # Tentukan break berikutnya (long break setelah 4 pomodoro, short break lainnya)
                    if pomodoro_streak >= POMODOROS_BEFORE_LONG_BREAK:
                        change_mode(LONG_BREAK_MODE)
                        pomodoro_streak = 0  # Reset streak
                    else:
                        change_mode(SHORT_BREAK_MODE)
                    
                    # Otomatis mulai break
                    started = True
                    
                elif current_mode == SHORT_BREAK_MODE or current_mode == LONG_BREAK_MODE:
                    # Setelah break, kembali ke mode pomodoro
                    change_mode(POMODORO_MODE)
                    # Otomatis mulai pomodoro berikutnya
                    started = True
    
    # Gambar latar belakang
    # Ubah warna background berdasarkan mode
    if current_mode == POMODORO_MODE:
        SCREEN.fill("#ba4949")  # Merah untuk fokus
    elif current_mode == SHORT_BREAK_MODE:
        SCREEN.fill("#38858a")  # Biru muda untuk short break
    else:  # LONG_BREAK_MODE
        SCREEN.fill("#397097")  # Biru tua untuk long break
        
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))  # Gambar background di tengah

    # Update dan tampilkan semua tombol
    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())  # Efek hover warna

    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())

    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())

    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())

    # Hitung menit dan detik dari current_seconds (pastikan tidak negatif)
    display_seconds = max(0, current_seconds % 60)
    display_minutes = max(0, int(current_seconds / 60) % 60)

    # Render teks timer dan tampilkan
    timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "#d48589")
    SCREEN.blit(timer_text, timer_text_rect)

    # Render total pomodoros yang selesai
    session_text = STAT_FONT.render(f"Sessions Completed: {completed_pomodoros}", True, "#d48589")
    SCREEN.blit(session_text, (WIDTH/2 - 150, HEIGHT/2 + 180))

    # Hitung total jam & menit dari total_seconds_focused
    total_minutes = total_seconds_focused // 60
    total_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

    # Render total waktu fokus
    time_text = STAT_FONT.render(f"Total time: {total_hours}h {remaining_minutes}m", True, "#d48589")
    SCREEN.blit(time_text, (WIDTH/2 - 150, HEIGHT/2 + 210))
    
    
    # Tampilkan semua update ke layar
    pygame.display.update()
    
    # Atur frame rate
    CLOCK.tick(60)