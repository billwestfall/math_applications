function Counter(inc) {
  var count = 0;
  var add = function() {
    count += inc;
    console.log('Current count: ' + count);
  }
  return add;
}

var inc2 = Counter(2);
inc2();
inc2();
