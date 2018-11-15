clear all
fs=load('fs.txt')
periodo=zeros(1,49)
frec=zeros(1,49)
for i=1:49
    file_name = sprintf('frec%d.txt',i);
    data = load(file_name)
    [pks, locs] = findpeaks(data)
    periodo(i)=mean(diff(locs))./fs(i+1)
    frec(i)=1/periodo(i)
    hold on
    plot(fs(i+1),frec(i),'b.','markersize',20)
    grid on
    xlabel('Frecuencia de muestreo (Hz)')
    ylabel('Frecuencia medida (Hz)')
    axis square
end

i=0
figure(2)
file_name = sprintf('frec%d.txt',i);
data = load(file_name)
[pks, locs] = findpeaks(data)
plot(data,'.-','markersize',10)
hold on
plot(locs,pks,'r.','markersize',20)
length(pks)
