# Builder

## Notes
    Builder pattern separates complex object creation from its representation.
        - Client can use the same construction process to create customized object representation
    Complex object: Object that consists of different combinations of objects
        - Complex object consists of one ore parts:   
            - object part a 
            - object part b 
            - object part c 
        
    
    Builder pattern allows for more complex creation of an object:
        - Object can have all or none of its properties
    
    Terminology:
        - Product           : The product being build 
        - Builder Interface : The interface that the Concrete Builder builder should implement
        - Builder           : Provides methods to build and retrieve Concrete Product 
        - Creator           : Has a construct() method that creates customized products using Builder methods aka Director 

    Builder and Director do not become an instance, they are used for static methods,   
    Implementation of Builder and Creator have static methods
    Builder's static methods return an instance of product 
    Director tells builder which parts should be in the product. 
    Builder has only so many parts. 
    

