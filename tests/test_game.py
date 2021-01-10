from final_project.final_project import application
import unittest



class TestPlayer(unittest.TestCase):

    def test_player_object_attribute_initialization(self):

        gamer_name = 'Anybody'
        player_info = {'name': 'Jimmy', 'age': 20, 'credit': 100}
        
        test_player = application.Players(gamer_name,player_info)

        assert hasattr(test_player, 'gamer_name'), 'Player has no gamer_name'
        assert hasattr(test_player, 'player_info'), 'Player has no informations'
        
    def test_players_get_name_method_returns_gamer_name(self):

        gamer_name = 'Anybody'
        player_info = {'name': 'Jimmy', 'age': 20, 'credit': 100}
        
        test_player = application.Players(gamer_name,player_info)

        assert test_player.get_name() == test_player.gamer_name, 'This is not the players gamer_name'

    def test_players_comparing_checks_players_credits(self):

        player1 = application.Players('Python', {'name':'py','age':10,'credit':100})
        player2 = application.Players('Pygame', {'name':'game','age':20,'credit':100})

        result = (player1==player2)

        self.assertEqual(result, player1["credit"]==player2["credit"]), 'Not the players credits are being verified' 



class Roulette(unittest.TestCase):
    
    def test_generated_number_is_correct(self):

        needed_colors = ['RED', 'BLACK']

        generate_random_color = application.generate_random()[1]
        
        self.assertIn(generate_random_color, needed_colors), 'Invalid color generated'


