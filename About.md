## Chess Algo

This programs impements a checkesrs algorithm.
Currently utilizes a Min-Max tree with alpha beta prusing to estimate the optimal move. Future improments incluse further optimizstions to this the effieincy of this tree as well as adding a machine learning based engine.
#### Current Features

- [x] Min max
  - [x] Alpha-beta pruning

#### Planned Features

- [ ] Search

  - [ ] Iterative Deepening
  - [ ] Aspiration Windows
  - [ ] Parallel Search using Threads
  
    - [ ] YBWC prior to Stockfish 
    - [ ] Lazy SMP since Stockfish 7, January 2016
  - [ ] Principal Variation Search
  - [ ] Transposition Table
  
    - [ ] Shared Hash Table
    - [ ] 10 Bytes per Entry, 3 Entries per Cluster
    - [ ] Depth-preferred Replacement Strategy
    - [ ] No PV-Node probing
    - [ ] Prefetch
  - [ ] Move Ordering
  
    - [ ] Countermove Heuristic
    - [ ] Counter Moves History since Stockfish 7, January 2016 [24]
    - [ ] History Heuristic
    - [ ] Internal Iterative Deepening
    - [ ] Killer Heuristic
    - [ ] MVV/LVA
    - [ ] SEE
  - [ ] Selectivity
  
    - [ ] Extensions
    
      - [ ] Check Extensions if SEE >= 0
      - [ ] Restricted Singular Extensions
    - [ ] Pruning
    
      - [ ] Futility Pruning
      - [ ] Move Count Based Pruning
      - [ ] Null Move Pruning
    
        - [ ] Dynamic Depth Reduction based on depth and value
        - [ ] Static Null Move Pruning
        - [ ] Verification search at high depths
      - [ ] ProbCut
      - [ ] SEE Pruning
    - [ ] Reductions
    
      - [ ] Late Move Reductions
      - [ ] Razoring
    - [ ] Quiescence Search
- [ ] Evaluation

  - [ ] Tapered Eval
  - [ ] Score Grain: ~1/256 of a pawn unit
  - [ ] Material

    - [ ] Point Values

      - [ ] Midgame: 198, 817, 836, 1270, 2521
      - [ ] Endgame: 258, 846, 857, 1278, 2558
    - [ ] Bishop Pair
    - [ ] Imbalance Tables
    - [ ] Material Hash Table
  - [ ] Piece-Square Tables
  - [ ] Space
  - [ ] Mobility

    - [ ] Trapped Pieces
    - [ ] Rooks on (Semi) Open Files
  - [ ] Outposts
  - [ ] Pawn Structure

    - [ ] Pawn Hash Table
    - [ ] Backward Pawn
    - [ ] Doubled Pawn
    - [ ] Isolated Pawn
    - [ ] Phalanx
    - [ ] Connected Pawns
    - [ ] Passed Pawn
  - [ ] King Safety

    - [ ] Attacking King Zone
    - [ ] Pawn Shelter
    - [ ] Pawn Storm
    - [ ] Square Control
  - [ ] Evaluation Patterns
 
 [StockFish](https://www.chessprogramming.org/Stockfish#Chess_engine)
