# Encoding

Basically, our model will change the state of a cell based on the neighborhood, where a cell corresponds to a single person.
A cell have two possible states: infected or healthy. If the state is infected, the cell will have X% of chance to get infected depending  on how many neighbors are infected. If healthy state, there will be a Y% chance of getting healthy depending on the number of infected neighbors.

|Number of Neighbors| N1 | N2 | N3 | N4 | N5 | N6 | N7 | N8 | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|**Healthy**| H1% | H2% | H3% | H4% | H5% | H6% | H7% | H8% | 
|**Infected**| I1% | I2% | I3% | I4% | I5% | I6% | I7% | I8% | 
