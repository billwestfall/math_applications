var obj = {a:3, b:2, c:4};
for (var prop in obj) {
  if( obj.hasOwnProperty( prop ) ) {
    process.stdout.write("o. " + prop + " = " obj[prop]);
  }
}
