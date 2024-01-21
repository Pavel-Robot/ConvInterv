n =2
m = 2
%l = 8
Num = 20000
command = 'ps -p 4996 v | grep "/mnt/games/Matlab" | awk ''{print $8}''';
[status, output] = system(command);
start_mem = str2double(output)/1024; %megabytes
times = [];
memory = [];
d_x = [];
for size=2:Num
    data = (1:size)';
    d_x = [d_x, size];
    tic
    intrlvr = comm.ConvolutionalInterleaver(NumRegisters=n,RegisterLengthStep=m);
    [status, output] = system(command);
    intrlvData = intrlvr(data);
    time = toc;
    
    end_mem = str2double(output)/1024; %megabytes
    memory = [memory, end_mem - start_mem];
    times = [times, time];
end
%
%figure;
%subplot(2,1,1);
%hold on;
%plot(d_x, times, '.');

%subplot(2,1,2)
%plot(d_x, memory, '.');

%title('Графики');
%xlabel('x');
%ylabel('y');
%hold off;

%intrlvData = intrlvr(data);
% создайте системный объект сверточного перемежителя, 
% указав количество регистров сдвига и шаг длины регистра.
intrlvr = comm.ConvolutionalInterleaver(NumRegisters=n, ...
                                        RegisterLengthStep=m);

%Создайте системный объект сверточного деперемежителя,
% указав количество регистров сдвига и шаг длины регистра.
deintrlvr = comm.ConvolutionalDeinterleaver(NumRegisters=n, ...
                                            RegisterLengthStep=m);

%Сгенерируйте случайную последовательность данных.
% Пропустите последовательность данных через перемежитель,
% а затем через деперемежитель.
%data = (1:l)';
%data = ones(16, 1);
intrlvData = intrlvr(data);
deintrlvData = deintrlvr(intrlvData);



% Вод результатов
disp('Объект:');
disp(intrlvr);
disp('Вход:');
disp(data);
disp('Выход(кодирование):');
disp(intrlvData);
disp('Выход(декодирование):');
disp(deintrlvData);
