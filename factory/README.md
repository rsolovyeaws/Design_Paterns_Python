# Factory

## NOTES:
    Factory design pattern abstracts object creation from its usage. 
    Concrete object is instantiated in the Creator class (vs in Client code).
    It hides the complications of instantiating extra objects.
    
    Terminology:
    - Concrete creator  : Client application (class or method that calls Creator(Factory)) 
    - Product interface : An interface that describes product's attributes and methods that Factory requires to create final product
    - Concrete Product  : The object that implements product interface (returned from the factory)
    - Creator           : The Factory class. Declares the factory method returned that returns object request from it