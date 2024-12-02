open Core

let filename = "lib/day1/input.txt"
let day1Input = In_channel.read_lines filename

let split_numbers input =
  (* Split the string on whitespace *)
  let numstr = String.split ~on:' ' input |> List.filter ~f:(fun s -> not (String.is_empty s)) in
  List.map numstr ~f:Int.of_string 

let numLists = List.map day1Input ~f:split_numbers

let l1 = List.map ~f:List.hd_exn numLists |> List.sort ~compare:compare
let l2 = List.map ~f:List.tl_exn numLists |> List.map ~f:List.hd_exn |> List.sort ~compare:compare

let diffs = List.map2_exn ~f:(-) l2 l1 |> List.map ~f:abs 

let resultP1 = List.fold ~init:0 ~f:( + ) diffs


let rec countExistance n lst = 
  match lst with 
  | h::t  ->if h = n  then 1 + countExistance n t
  else countExistance n t
  | [] -> 0

let counts = List.map ~f:(fun a -> countExistance a l2) l1
let simScores = List.map2_exn ~f:( * ) l1 counts

let  resultP2 = List.fold ~f:(+) ~init:0 simScores