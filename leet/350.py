def intersect(self, nums1, nums2):
    li = []
    for i in nums1:
        if i in nums2:
            li.append(i)
            nums2.remove(i)

    return li
