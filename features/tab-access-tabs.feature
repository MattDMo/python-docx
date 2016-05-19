Feature: Adjust tab stops
  In order to customize tab stops for a paragraph or style
  As a developer using python-docx
  I need ways to create, read, update, and remove tab stops


  Scenario Outline: Count tab stop objects
    Given a tab_stops having <count> tab stops
     Then len(tab_stops) is <count>

    Examples: values for tab_stop elements
      | count |
      | 0     |
      | 3     |


  Scenario: Access an individual tab stops
    Given a tab_stops having 3 tab stops
     Then I can iterate over the tab stop objects it contains
      And I can access a tab stop by index


  @wip
  Scenario Outline: Add a tab stop
    Given a tab_stops having <count> tab stops
     When I add a tab stop
     Then len(tab_stops) is <new-count>
      And the tab stops are sequenced in position order

    Examples: tab stop object counts
      | count | new-count |
      |   0   |     1     |
      |   3   |     4     |


  @wip
  Scenario: Remove a tab stop
    Given a tab_stops having 3 tab stops
     When I remove a tab stop
     Then len(tab_stops) is 2
      And the removed tab stop is no longer present in tab_stops


  @wip
  Scenario: Clear tab stops
    Given a tab_stops having 3 tab stops
     When I call tab_stops.clear_all()
     Then len(tab_stops) is 0
