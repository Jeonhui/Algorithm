//
//  main.swift
//  lv0
//
//  Created by 이전희 on 2023/05/18.
//

import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (a, b) = (n[0], n[1])

print(a + b)

