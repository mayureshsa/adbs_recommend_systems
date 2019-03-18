##Cypher Queries to generate the Neo4j Graph:
![alt text](https://github.com/mayureshsa/adbs_recommend_systems/blob/master/neo4j_graph.svg)

Enter these Cypher queries in the Neo4j browser one by one:

CREATE (s1:Student{name:'Adam'}) – [:TAKES] ->(course:Course {title:'Database systems', code:'c1'})

CREATE (s2:Student{name:'Bob'})
MATCH (s2:Student {name:'Bob'}), ((course:Course {code:'c1'})) MERGE (s2)-[:TAKES]-> (course)

MERGE (s2:Student{name:'Bob'}) CREATE (s2) - [:TAKES] -> (course:Course{title:'Machine Learning', code:'c2'})

CREATE (s3:Student{name:'Tom'})
MATCH (s3:Student {name:'Tom'}), ((course:Course {code:'c2'})) MERGE (s3)-[:TAKES]-> (course)

MERGE (s3:Student{name:'Tom'}) CREATE (s3) - [:TAKES] -> (course:Course{title:'Statistics', code:'c3'})

CREATE (d1:Department{name:'Computer Science', dept_code:'CS2019'})
MATCH (c1:Course {title:'Database systems', code:'c1'}), (d1:Department{dept_code:'CS2019'}) MERGE (c1)-[:BELONGS]-> (d1)

MATCH (course:Course{title:'Machine Learning', code:'c2'}), ((d1:Department{dept_code:'CS2019'})) MERGE (course)-[:BELONGS]-> (d1)

CREATE (d2:Department{name:'Mathematics', dept_code:'MT2019'})
MATCH (c2:Course{title:'Machine Learning', code:'c2'}), (d2:Department{dept_code:'MT2019'}) MERGE (c2)-[:BELONGS]-> (d2)

MATCH (course:Course{title:'Statistics', code:'c3'}), ((d2:Department{dept_code:'MT2019'})) MERGE (course)-[:BELONGS]-> (d2)

CREATE (course:Course {title:'Database Mining', code:'c4'})
MATCH (course:Course {title:'Database Mining', code:'c4'}), ((d1:Department{name:'Computer Science', dept_code:'CS2019'})) MERGE (course)-[:BELONGS]-> (d1)


## now the hunt is on
match (s1:Student {name:'Tom'}) - [:TAKES] -> (s1) RETURN (s1)

## find people who took the same course as Tom
match (s1:Student {name:'Tom'}) - [:TAKES] -> (c2) <- [:TAKES] - (s) RETURN (s)

## find courses taken by the people who took same course as Tom
match (s3:Student {name:'Tom'}) - [:TAKES] -> (c2) <- [:TAKES] - (s2) - [:TAKES] -> (p3) RETURN p3

## find departments that belong to courses taken by Tom
match (s3:Student {name:'Tom'}) - [:TAKES] -> (c2) - [:BELONGS] -> (d) RETURN (d)
