open Core

(* let filename = "lib/day2/example.txt" *)
let filename = "lib/day2/input.txt"
let day2Input = In_channel.read_lines filename

let reportFromLine line = String.split ~on:' ' line |> List.map ~f:int_of_string

let reports = List.map ~f:reportFromLine day2Input

let rec makeDiffs lst = 
  match lst with
  | a :: b ::  t -> a-b::(makeDiffs (b::t))
  | [_] -> []
  | [] ->[]

let isSafePos lst = List.for_all ~f:(fun a -> a >= 1 && a <=3) lst
let isSafeNeg lst = List.for_all ~f:(fun a -> a <= -1 && a >= -3) lst

let isSafe lst = isSafeNeg lst || isSafePos lst

let diffs = List.map ~f:makeDiffs reports
let safes = List.map ~f:isSafe diffs
let resultP1 = List.count ~f:Fn.id  safes

let remove_one_at_a_time lst =
  List.mapi ~f:(fun i _ -> List.filteri ~f:(fun j _ -> i <> j) lst) lst

let isSafeWithOneRemoved lst = 
  let lstWithOneRemoved = remove_one_at_a_time lst in
  let diffsWithOneRemoved = List.map ~f:makeDiffs lstWithOneRemoved in
  let safeList = List.map ~f:isSafe diffsWithOneRemoved in
  List.fold ~init:false ~f:( || ) safeList

let safesP2 = List.map ~f:isSafeWithOneRemoved reports

let resultP2 = List.count ~f:Fn.id safesP2
