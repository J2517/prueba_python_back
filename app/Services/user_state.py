class UserState:
    """
        Clase para gestionar el estado del último usuario consultado en la aplicación.
        Implementa el patrón Singleton para garantizar que solo exista una instancia única.
    """
    _instance = None
    
    def __new__(cls):
        """
            Método para controlar la creación de instancias de la clase.
            Si no existe una instancia, la crea y la inicializa; de lo contrario, retorna la ya existente.
        """
        if cls._instance is None:
            cls._instance = super(UserState, cls).__new__(cls)
            cls._instance.last_queried_user = {"id": None, "data": None}
        return cls._instance
    
    def set_last_user(self, user_id: int, user_data: dict):
        self.last_queried_user = {"id": user_id, "data": user_data}
    
    def get_last_user(self):
        return self.last_queried_user
    
    def has_user(self):
        """
        Verifica si existe información de un usuario consultado.

        Returns:
            bool: True si hay un usuario registrado, False en caso contrario.
        """        
        return self.last_queried_user["id"] is not None