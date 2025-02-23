from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "123456789"  # 替换为你的实际密码

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Hello Neo4j!' AS message")
        print(result.single()["message"])

test_connection()  # 输出: Hello Neo4j!

def create_person(name, age):
    with driver.session() as session:
        query = """
        CREATE (p:Person {name: $name, age: $age})
        RETURN p
        """
        result = session.run(query, name=name, age=age)
        return result.single()

# create_person("Charlie", 28)

def find_person(name):
    with driver.session() as session:
        query = """
        MATCH (p:Person {name: $name})
        RETURN p.name AS name, p.age AS age
        """
        result = session.run(query, name=name)
        return [record for record in result]

print(find_person("Alice"))  # 输出: []
print(find_person("Charlie"))  # 输出: [<Record name='Charlie' age=28>]

# create_person("Alice", 30)

def create_friendship(name1, name2):
    with driver.session() as session:
        query = """
        MATCH (a:Person {name: $name1}), (b:Person {name: $name2})
        CREATE (a)-[r:FRIEND]->(b)
        RETURN type(r)
        """
        result = session.run(query, name1=name1, name2=name2)
        return result.single()

# create_friendship("Alice", "Charlie")

def complex_transaction():
    with driver.session() as session:
        tx = session.begin_transaction()
        try:
            tx.run("CREATE (:Book {title: 'Neo4j Guide'})")
            tx.run("MATCH (b:Book) WHERE b.title = 'Neo4j Guide' SET b.price = 39.99")
            tx.commit()
        except Exception as e:
            tx.rollback()

# complex_transaction()