#Standardization(5)

scores =[[10, 15, 20], [20, 25, 30], [30, 35, 40], [40, 45, 50]]

n_student = len(scores)
n_class = len(scores[0])

class_score_sums = list()
class_score_square_sum = list()
class_mean = list()


class_score_variance = list()
class_score_std = list()


# set the sum of class scores as 0
for _ in range(n_class):
    class_score_sums.append(0)
    class_score_square_sum.append(0)
    class_score_variance.append(0)
    class_score_std.append(0)
# classes' sums, squared sums

for student_scores in scores:
    for class_idx in range(n_class):
        class_score_sums[class_idx] += student_scores[class_idx]
        class_score_square_sum[class_idx] += student_scores[class_idx]**2
print("class score sums: ", class_score_sums)
print("class score square sum: ", class_score_square_sum)

## classes' varinaces
for class_idx in range(n_class):

    mos = class_score_square_sum[class_idx] / n_student
    som = (class_score_sums[class_idx] / n_student)**2
    class_mean.append(class_score_sums[class_idx] / n_student)
    class_score_variance[class_idx] = mos-som
    class_score_std[class_idx] = (mos-som)**0.5

print(f'Variances: {class_score_variance}')
print(f'Std : {class_score_std}')
print(f'mean : {class_mean}')
print(scores)
# Standardization
for student_idx in range(n_student):
    for class_idx in range(n_class):
        score = scores[student_idx][class_idx]
        mean = class_mean[class_idx]
        std = class_score_std[class_idx]
        scores[student_idx][class_idx] = (score - mean)/std


sd_class_score_sums = list()
sd_class_score_square_sum = list()
sd_class_mean = list()


sd_class_score_variance = list()
sd_class_score_std = list()

for _ in range(n_class):
    sd_class_score_sums.append(0)
    sd_class_score_square_sum.append(0)
    sd_class_score_variance.append(0)
    sd_class_score_std.append(0)

for student_scores in scores:
    for class_idx in range(n_class):
        sd_class_score_sums[class_idx] += student_scores[class_idx]
        sd_class_score_square_sum[class_idx] += student_scores[class_idx]**2


for class_idx in range(n_class):

    mos = sd_class_score_square_sum[class_idx] / n_student
    som = (sd_class_score_sums[class_idx] / n_student)**2
    sd_class_mean.append(sd_class_score_sums[class_idx] / n_student)
    sd_class_score_variance[class_idx] = mos-som
    sd_class_score_std[class_idx] = (mos-som)**0.5

print(f'Variances: {sd_class_score_variance}')
print(f'Std : {sd_class_score_std}')
print(f'mean : {sd_class_mean}')