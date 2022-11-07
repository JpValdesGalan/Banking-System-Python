class Client:
    
    id_counter = 1 # Keeps track of ids
    
    ''' Client Constructor '''
    def __init__(self, name: str, address: str) -> None:
        ''' Defines the Client values'''
        self.id = Client.id_counter
        self.name = name
        self. address = address
        Client.id_counter += 1
        
    ''' Get Methods '''
    def get_id(self) -> str:
        ''' Returns the Client id '''
        return self.id
    
    def get_name(self) -> str:
        ''' Returns the Client name '''
        return self.name
    
    def get_address(self) -> str:
        ''' Returns the Client address '''
        return self.address
    
    ''' Set Methods'''
    def set_name(self, new_name) -> None:
        ''' Updates the Client name value '''
        self.name = new_name
        
    def set_address(self, new_address) -> None:
        ''' Updates the Client address value '''
        self.address = new_address
        
    ''' Client Methods '''
    def show(self) -> None:
        ''' The show method prints the details of the Client '''
        print(f'Cliente\n'
              f'Id: {self.id:06}\n'
              f'Name: {self.name}\n'
              f'Address: {self.address}\n')