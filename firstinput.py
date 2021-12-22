def info(time, name, gender, age, activity):
    numbers_dic = {0: [1, 0.5, 3, 1.5, 3, 2, 3, 1], 1: [1, 1.5, 4, 1.5, 3, 2, 3, 1], 2: [1, 2, 5, 1.5, 3, 2, 4, 1], 3: [
        1, 2, 6, 1.5, 4, 3, 5, 1], 4: [1.5, 2, 6, 1.5, 4, 3.5, 5, 1], 5: [1.5, 2.5, 7, 1.5, 5, 4, 6, 1], 6: [1.5, 2.5, 8, 2, 5, 4, 7, 1]}
    status_lst = [['130'], ['030', '100', '110', '120', '111', '121', '131'], ['000', '010', '020', '031', '101', '122', '132', '133'], [
        '011', '021', '032', '102', '112', '113', '123', '033'], ['001', '022', '103'], ['002', '102', '023'], ['003', '013']]
    code = str(gender) + str(age) + str(activity)
    target = []
    for status in status_lst:
        if code in status:
            target = numbers_dic.get((status_lst.index(status)))
            target.insert(0, time)
            target.insert(1, name)
            break
    return target