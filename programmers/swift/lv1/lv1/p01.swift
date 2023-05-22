//
//  p01.swift
//  lv1
//
//  Created by 이전희 on 2023/05/18.
//

// 달리기 경주
import Foundation

struct p01 {
    let players = ["mumu", "soe", "poe", "kai", "mine"]
    let calling = ["kai", "kai", "mine", "mine"]
    let result = ["mumu", "kai", "mine", "soe", "poe"]
    
    func solution(_ players:[String], _ callings:[String]) -> [String] {
        callings.reduce(players) { partialResult, call in
            var players = partialResult
            if let i = players.firstIndex(of: call) {
                (players[i-1], players[i]) = (players[i], players[i-1])
            }
            return players
        }
    }
    
    func run(){
        print(solution(players, calling))
    }
}
