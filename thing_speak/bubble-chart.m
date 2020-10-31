readAPIKey = 'V79KCD77H54DO184';
readChannelID = 1213641;

fieldID1 = 1;
fieldID2 = 2;
fieldID3 = 3;

device_id = 1;

array_id = thingSpeakRead(readChannelID, 'Field', fieldID1, 'NumPoints', 300, 'ReadKey', readAPIKey);
array_x = thingSpeakRead(readChannelID, 'Field', fieldID2, 'NumPoints', 300, 'ReadKey', readAPIKey);
array_y = thingSpeakRead(readChannelID, 'Field', fieldID3, 'NumPoints', 300, 'ReadKey', readAPIKey);

new_x_array = {};
new_y_array = {};
new_z_array = {};

for index = 1:length(array_x)
    index_item_x = array_x(index);
    index_item_y = array_y(index);

    if array_id(index) ~= device_id
        continue;
    end
    
    if index == 1    
        new_x_array{1} = index_item_x;
        new_y_array{1} = index_item_y;
        new_z_array{1} = 1;
    else        
        
        already_exists_index = -1;
        
        for index2 = 1:length(new_x_array)
           index2_item_x = new_x_array(index2);
           index2_item_y = new_y_array(index2);
           
           if((index_item_x == cell2mat(index2_item_x)) && (index_item_y == cell2mat(index2_item_y)))
                already_exists_index = index2;
           end
        end
        
        if already_exists_index == -1
            new_x_array{length(new_x_array) + 1} = index_item_x;
            new_y_array{length(new_y_array) + 1} = index_item_y;
            new_z_array{length(new_z_array) + 1} = 1; 
        else
            new_z_array{already_exists_index } = new_z_array{index2} + 1;
        end 
    end
end

bubblechart(cell2mat(new_x_array), cell2mat(new_y_array), cell2mat(new_z_array), 'red');
bubblesize([20 50]);