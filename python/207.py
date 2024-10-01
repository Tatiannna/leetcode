# 207. Course Schedule

# https://leetcode.com/problems/course-schedule/description/

# todo
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # is there AT LEAST ONE path (a specific sequence of courses to take) 
        # that can traverse through all NUM courses in 

        # Course C can be taken iff there is a path to it (with no cycles)
        # If there is a cycle AND there are still classes that have not been taken, return False
        # If there is no cycle and still some classes have not been taken, return false
        # Return true when you come across a path that includes all NUM courses


        class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def take_course_if_possible(course, s = set()): # return true if there is no prereq, else recursively call dfs on the prereq
            if course not in pres: # no pre rec, so course can be taken
                taken.add(course)
                return True
            if course in taken:  # course already take, so return true
                return True
            else: # if course is not taken, go through each pre req, and see if taking the course is possible
                for c in pres[course]:
                    if c in s: # this course is already in the chain
                        return False
                    if c not in taken:
                        # is there a cycle down this path? - does the chain of prereqs ultimately return to c?
                        new_set = s.union({c})
                        return take_course_if_possible(c,new_set)
                    else:# this particular prereq was already taken
                        taken.add(c)
                        return True

        # combinations = set()
        pres = defaultdict(list)
        taken = set()
        # queue = [taken]

        for courses in prerequisites:
            pres[courses[0]].append(courses[1])

        for courses in prerequisites:
            course = courses[0]
            if take_course_if_possible(course):
                taken.add(course)
            else:
                return False
        return 

        # # for course, prereq in pres:
        # #     if prereq not in taken and

        # for courses in prerequisites:
        #     course = courses[0]

        #     # for each pre req
        #         # check if it has prereqs
        #         # ensure no cycle
            
        #     # if current course has at least 1 prereq
        #     if course in pres:
        #         i = 0
        #         # for each prereq
        #         temp = course
        #         while i < len(pres[course]):
        #             course_subset = set() # course not added to set because its not 'taken' until prereqs are taken first
        #             while course in pres:
        #                 course = pres[course][i]
        #                 if course not in course_subset:
        #                     course_subset.add(course)
        #                 else:
        #                     return False
        #             i += 1
        # return True


        

            
            
        # while queue:
        #     current_taken_set = queue.pop()

        #     if len(current_taken_set) == numCourses:
        #         return True
        #     for course in range(numCourses):
        #         if course not in current_taken_set:
        #             # if there is no prereq or if prereq was taken, add course
        #             if course not in pres or pres[course] in current_taken_set:
        #                 curr_copy = current_taken_set.copy()
        #                 curr_copy.add(course)
        #                 queue.append(curr_copy)
        #             else:
        #                 prereq_chain = set()
        #                 temp = course
        #                 while course in pres:
        #                     if pres[course] not in prereq_chain:
        #                         prereq_chain.add(pres[course])
        #                         course = pres[course]
        #                     else:
        #                         return False
        #                 prereq_chain.add(temp)
        #                 u = current_taken_set.union(prereq_chain)
        #                 queue.append(u)
        # return False