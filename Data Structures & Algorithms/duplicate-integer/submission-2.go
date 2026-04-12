func hasDuplicate(nums []int) bool {
    mySet := make(map[int]bool)

    for _, num := range nums {
        if _,ok := mySet[num]; ok{
            return true
        }
        mySet[num] = true
    }
    return false
}
