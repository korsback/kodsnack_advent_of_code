open Core 

(* let filename = "lib/day3/example.txt" *)
let filename = "lib/day3/input.txt"
let day3Input = In_channel.read_all filename

let regex =  Re2.create_exn "mul\\((\\d+),(\\d+)\\)" 

let calc str = 
  let f1 = List.map ~f:int_of_string (Re2.find_all_exn ~sub:(`Index 1) regex str) in
  let f2 = List.map ~f:int_of_string (Re2.find_all_exn ~sub:(`Index 2) regex str) in
  let muls = List.map2_exn ~f:( * ) f1 f2 in 
  muls

let resultP1 = List.fold ~init:0 ~f:(+) (calc day3Input)

let startDisable = "don't()"
let stopDisable = "do()"

let removePart str = 
  let start = String.substr_index ~pattern:startDisable str in

  match start with 
  | Some start -> 
    (* don't() is found. Now search for next do() from that point*)
    let afterStr = String.sub str ~pos:(start + String.length startDisable ) ~len:(String.length str - (start+String.length startDisable)) in
    let stop = String.substr_index ~pattern:stopDisable afterStr in
     ( match stop with 
      | Some stop ->
      (* do() is found. Return the parts before and after.*)
        let before =  String.sub str ~pos:0 ~len:start in
        let after = String.sub afterStr ~pos:(stop + String.length stopDisable) ~len:(String.length afterStr - (stop+String.length stopDisable)) in
           true, before ^ after
      | None ->
        (* do() is not found. Return everything before don't()*)
        true, String.sub str ~pos:0 ~len:start)
  | None ->  false, str

let removeDisabled str = 
  let rec inner s = 
    let res = removePart s in
    match res with 
    | false, st -> st
    | true, st -> inner st
  in
  inner str

let removeLast str = 
  let lasti = String.substr_index ~pattern:startDisable str in
  match lasti with 
  | Some i -> String.sub str ~pos:0 ~len:i
  | None -> str

let part2 = removeDisabled day3Input
let part2 = removeLast part2

let resultP2 =  List.fold ~init:0 ~f:(+) (calc part2)
