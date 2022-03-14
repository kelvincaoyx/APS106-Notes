
def check_score(box_score):
    '''
    (list) -> Bool
    Checks the the box_score is well-formed. 
    - That the goals in each period sum to the total and
    - The correct team is listed as winning.
    If these are correct, True is returned. If incorrect, False is returned.
    '''
    final_score = []
    
    # check if scores add up
    for team in box_score[:2]:
        if sum(team[1][:3]) != team[1][3]:
            return False
        final_score.append(team[1][3])
    
    # check if right team won
    winner = box_score[0][0]
    if final_score[0] < final_score[1]:
        winner = box_score[1][0]
        
    return winner == box_score[2]

box_scores = [[["MTL", [1, 0, 0, 1]], ["TOR", [1,0,1,2]], "TOR"],
              [["VAN", [1, 2, 0, 3]], ["CGY", [1,1,0,4]], "CGY"],
              [["EDM", [18, 0, 0, 18]], ["OTT", [0, 0,0,0]], "EDM"],
              [["TOR", [3, 0, 0, 3]], ["OTT", [0, 0,0,0]], "OTT"]]

for score in box_scores:
    print(check_score(score))