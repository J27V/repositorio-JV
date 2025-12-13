import time

def escribir(texto, pausa=0.06):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(pausa)
    print()

print("\n💖✨  PARA MI QUERIDA  ESMERALDA ✨💖\n")
time.sleep(1)

escribir("Mi  pricesa hermosa 💚")
time.sleep(0.8)

escribir("Gracias por llegar a mi vida,")
escribir("por llenar mis días de luz,")
escribir("y mi corazón de amor.")
time.sleep(1)

print()
escribir("Desde que estás conmigo:")
escribir("🌸 sonrío más")
escribir("💞 sueño más")
escribir("❤️ amo más")
time.sleep(1)

print()
escribir("No eres solo parte de mi vida...")
escribir("eres mi lugar favorito  y seguro 🏡")
time.sleep(1)

print("\n" + "💚" * 20)
escribir("TE AMO, MI PEQUEÑA 💖", 0.1)
print("💚" * 20)

print("\nGracias por existir ✨")