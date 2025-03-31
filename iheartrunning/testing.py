from unittest.mock import MagicMock

class IUserRepository:
    def save_score(self, name: str, score: int):
        pass
    
    def get_top_scores(self):
        pass

# Создание mock-объекта
mock_user_repository = MagicMock(spec=IUserRepository)

# Настройка поведения mock-объекта
mock_user_repository.get_top_scores.return_value = [("Player1", 100), ("Player2", 90)]

# Использование mock-объекта в тестах
print(mock_user_repository.get_top_scores())  # [('Player1', 100), ('Player2', 90)]
mock_user_repository.save_score("TestPlayer", 50)
mock_user_repository.save_score.assert_called_with("TestPlayer", 50)
