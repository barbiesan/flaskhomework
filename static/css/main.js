funcion check_me(input_id){
  var checked_input = document.querySelector("input[id=" + input_id + "]");
  var checked_label = document.querySelector("label[id=" + input_id + "]");

  if(checked_input.checked){
    checked_label.style.textDecoration = "line-through";
  }
  else {
    checked_label.style.textDecoration = "";
  }

  var btn = document.getElementById("remove_btn");
  
  btn.value ="REMOVE ITEMS";
  btn.style.color= "white";
  btn.style.backgroundColor = "black";
  btn.style.cursor = "pointer";
}