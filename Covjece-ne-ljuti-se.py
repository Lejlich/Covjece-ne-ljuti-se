import random

# Inicijalizacija igrača
players = ["Igrač", "Računar"]
player_positions = [0, 0]
player_turn = 0  # 0 je za igrača, 1 je za računar

# Pravila igre
def move_player(player):
    roll = random.randint(1, 6)  # Igrač baca kocku
    print(f"{players[player]} je bacio kocku i dobio {roll}.")
    return roll

# Glavna petlja igre
def play_game():
    while True:
        # Računar ili igrač na potezi
        print(f"\nTrenutne pozicije: {players[0]}: {player_positions[0]}, {players[1]}: {player_positions[1]}")
        
        move = move_player(player_turn)
        player_positions[player_turn] += move
        
        if player_positions[player_turn] >= 30:  # Ako neko dostigne ili pređe 30
            print(f"\n{players[player_turn]} je pobedio!")
            break
        
        # Prebacivanje na sledećeg igrača
        player_turn = 1 - player_turn  # Ako je sada igrač, sledeći je računar i obrnuto

if __name__ == "__main__":
    play_game()
