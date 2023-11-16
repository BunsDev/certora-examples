methods {
  function _.set1() external => NONDET;
  function _.set2() external => HAVOC_ALL;
  function getFromG1() external returns (uint256) envfree;
  function getFromG2() external returns (uint256) envfree;
}​

/***
 check which function changes which variable in intGetterImpl 
 due to the summarize of set1 as nondet set1() does not change and varaible 

 */
rule checkChange(method f) {
  uint256 g1Before = getFromG1();
  uint256 g2Before = getFromG2();

  env e;
  calldataarg args;
  f(e,args);

  uint256 g1After = getFromG1();
  uint256 g2After = getFromG2();
  assert (g1Before == g1After, "get1 changed"); // Should fail only on set2
  assert (g2Before == g2After, "get2 changed"); // Should fail only on set2

}




